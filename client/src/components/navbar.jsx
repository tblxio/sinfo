import React from 'react'
import { bool } from 'prop-types'

const iconPath = process.env.PUBLIC_URL + '/media/icons/'

const Navbar = ({ connected = false, mobile = false }) => (
  <header className="Navbar">
    <div className="Navbar-container">
      <div className="Navbar-logo">
        {mobile ? (
          <img
            className="Navbar-logo-png"
            src={`${iconPath}logo-mobile.png`}
            alt="TDH"
          />
        ) : (
          <img
            className="Navbar-logo-svg"
            src={`${iconPath}logo.svg`}
            alt="TDH"
          />
        )}
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
  connected: bool,
  mobile: bool
}

export default Navbar
