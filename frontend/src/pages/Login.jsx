import LoginForm from "../components/LoginForm";

function Login({ onLoginSuccess }) {
  // Pass it down to your LoginForm
  return <LoginForm route="/api/token/" method="login" onLoginSuccess={onLoginSuccess} />;
}
export default Login;
