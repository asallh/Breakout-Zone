import "./App.css";
import styled from "styled-components";

export default function App() {
  const title = "Welcome to Breakout Zone";
  return (
    <>
      <div className="app">
        <div className="content">
          <h1 className="heading-title">{title}</h1>
          <h2 className="sub-heading">See you soon.</h2>
        </div>
      </div>
    </>
  );
}
