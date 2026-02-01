import LoginForm from "../components/LoginForm";

function Login({ onLoginSuccess }) {
  return <LoginForm route="/auth/login/access-token" method="login" onLoginSuccess={onLoginSuccess} />;
}
export default Login;
