import { useEffect, useState } from "react";
import io from "socket.io-client";
let socket;

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  useEffect(() => {
    socket = io("http://localhost:5000");
    socket.on("receive_message", (msg) => {
      setMessages((prev) => [...prev, msg]);
    });
    return () => socket.disconnect();
  }, []);
  function sendMessage() {
    socket.emit("send_message", { message: input });
    setInput("");
  }
  return (
    <div>
      <h2>Qryptik Chat</h2>
      <ul>
        {messages.map((msg, i) => (
          <li key={i}>{msg.message}</li>
        ))}
      </ul>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
