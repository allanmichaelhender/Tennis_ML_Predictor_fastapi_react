import LoginForm from "../components/LoginForm";

function Login({ onLoginSuccess }) {
  return <LoginForm route="/api/token/" method="login" onLoginSuccess={onLoginSuccess} />;
}
export default Login;
