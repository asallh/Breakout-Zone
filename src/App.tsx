import "./index.css";
import NavBar from "./components/NavBar";
import Home from "./components/HomeContent";
import { Switch } from "./components/ui/switch";

export default function App() {
  const title = "Welcome to Breakout Zone";
  return (
    <div className="app">
      <div className="content">
        <h1 className="heading-title">{title}</h1>
        <NavBar />
        <h2 className="sub-heading">See you soon.</h2>
        <Home />
      </div>
    </div>
  );
}
