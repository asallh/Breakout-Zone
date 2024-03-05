export default function NavBar() {
  return (
    <nav className="navbar">
      <div className="links">
        <a href="/">Home</a>
        <a
          href="/about"
          style={{
            paddingLeft: 56,
          }}
        >
          About
        </a>
      </div>
    </nav>
  );
}
