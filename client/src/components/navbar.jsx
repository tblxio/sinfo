import React from 'react'
import { bool } from 'prop-types'

const iconPath = process.env.PUBLIC_URL + '/media/icons/'

const Navbar = ({
  connected = false,
  mobile = false,
  harshAccel = false,
  harshTurn = false
}) => (
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

      <div className="Navbar-signals">
        <svg
          className={`Navbar-signals-icon ${
            harshAccel ? 'Navbar-signals-icon--active' : ''
          }`}
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path d="M0 0h24v24H0z" fill="none" />
          <path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z" />
        </svg>
        <svg
          className={`Navbar-signals-icon ${
            harshTurn ? 'Navbar-signals-icon--active' : ''
          }`}
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
        >
          <path d="M21.71 11.29l-9-9c-.39-.39-1.02-.39-1.41 0l-9 9c-.39.39-.39 1.02 0 1.41l9 9c.39.39 1.02.39 1.41 0l9-9c.39-.38.39-1.01 0-1.41zM14 14.5V12h-4v3H8v-4c0-.55.45-1 1-1h5V7.5l3.5 3.5-3.5 3.5z" />
          <path d="M0 0h24v24H0z" fill="none" />
        </svg>
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
  mobile: bool,
  harshAccel: bool,
  harshTurn: bool
}

export default Navbar
