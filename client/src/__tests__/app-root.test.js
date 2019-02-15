import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import { BrowserRouter } from 'react-router-dom'
import rootReducer from '../root-reducer'
import AppRoot from '../app-root.jsx'

const initialState = {}
const store = createStore(rootReducer, initialState)

describe('AppRoot Component', () => {
  beforeAll(() => {
    Object.defineProperty(window, 'matchMedia', {
      value: jest.fn(() => ({ matches: true }))
    })
  })

  it('should render routes component', () => {
    const el = document.createElement('div')
    ReactDOM.render(
      <Provider store={store}>
        <BrowserRouter>
          <AppRoot />
        </BrowserRouter>
      </Provider>,
      el
    )
    ReactDOM.unmountComponentAtNode(el)
  })
})
