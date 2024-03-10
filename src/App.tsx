import "./index.css";
import NavBar from "./components/NavBar";
import Home from "./components/HomeContent";

export default function App() {
  const title = "Welcome to Breakout Zone";
  return (
    <div className="app">
      <div className="content">
        <h1 className="font-bauer">{title}</h1>
        <NavBar />
        <h2 className="font-bauer">See you soon.</h2>
        <Home />
      </div>
    </div>
  );
}
