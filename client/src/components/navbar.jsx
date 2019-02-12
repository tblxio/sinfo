import React from 'react'
import { bool } from 'prop-types'

const iconPath = process.env.PUBLIC_URL + '/media/icons/'

const Navbar = ({ connected = false }) => (
  <header className="Navbar">
    <div className="Navbar-container">
      <div className="Navbar-logo">
        <img
          className="Navbar-logo-svg"
          src={`${iconPath}logo.svg`}
          alt="TDH"
        />
      </div>
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
