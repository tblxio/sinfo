import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { BrowserRouter } from 'react-router-dom'
import configureStore from './store'
import AppRoot from './app-root.jsx'
import './styles/index.scss'

const store = configureStore()

const App = () => (
  <Provider store={store}>
    <BrowserRouter>
      <div>
        <main className="main-content">
          <AppRoot />
        </main>
      </div>
    </BrowserRouter>
  </Provider>
)

ReactDOM.render(<App />, document.getElementById('app'))
