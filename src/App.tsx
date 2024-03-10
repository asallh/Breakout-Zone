import "./index.css";
import Home from "./components/HomeContent";
import NavBar from "./components/NavBar";

export default function App() {
  const title = "Breakout Zone";
  return (
    <div className="app">
      <div className="">
        {/* Team Selection Bar */}
        <NavBar />
        {/* Where the cards get rendered */}
        <Home />
      </div>
    </div>
  );
}
