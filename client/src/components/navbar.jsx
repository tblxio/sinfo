import React from 'react'
import { bool } from 'prop-types'

const Navbar = ({ connected = false }) => (
  <header className="Navbar">
    <div className="Navbar-container">
      <div className="Navbar-logo" />
      <div className="Navbar-status">
        <span className="Navbar-status-text">
          {connected ? 'Connected' : 'Disconnected'}
        </span>
        <div
          className={`Navbar-status-circle ${
            !connected ? `Navbar-status-circle--disconnected` : ``
          }`}
        />
      </div>
    </div>
  </header>
)

Navbar.propTypes = {
  connected: bool
}

export default Navbar
