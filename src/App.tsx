import "./index.css";
import Home from "./components/HomeContent";
import NavBar from "./components/NavBar";

export default function App() {
  const title = "Breakout Zone";
  return (
    <div className="py-16">
      {/* Team Selection Bar */}
      <NavBar />
      <div className="p-8">
        {/* Where the cards get rendered */}
        <Home />
      </div>
    </div>
  );
}
