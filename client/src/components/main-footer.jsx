import React from 'react'
const MainFooter = () => (
  <footer className="MainFooter">
    <div className="MainFooter-container">
      <a className="MainFooter-link" href="https://techhublisbon.io">
        know more about us
      </a>
      <p className="MainFooter-copyright">
        {new Date().getFullYear()} &copy; TECH + DATA HUB
      </p>
    </div>
  </footer>
)

export default MainFooter
