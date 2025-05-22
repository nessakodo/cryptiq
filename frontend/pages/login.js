import { useRouter } from "next/router";
export default function Login() {
  const router = useRouter();
  function handleLogin() {
    router.push("/chat");
  }
  return (
    <div>
      <h2>Login</h2>
      <button onClick={handleLogin}>Sign In (Demo)</button>
    </div>
  );
}
