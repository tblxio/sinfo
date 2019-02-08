import { createStore, applyMiddleware, compose } from 'redux'
import createHistory from 'history/createBrowserHistory'
import createSagaMiddleware from 'redux-saga'
import rootSaga from './sagas/root-saga'
import rootReducer from './root-reducer'

export default function configureStore(initialState = {}) {
  const history = createHistory()
  const enhancers = []
  const sagaMiddleware = createSagaMiddleware()
  const middleware = []
  const composeEnhancers =
    process.env.NODE_ENV === 'development' &&
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
      ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
      : compose

  middleware.push(sagaMiddleware)
  enhancers.unshift(applyMiddleware(...middleware))

  const store = createStore(
    rootReducer,
    initialState,
    composeEnhancers(...enhancers)
  )

  if (module.hot) {
    module.hot.accept('./root-reducer', () => {
      store.replaceReducer(rootReducer)
    })
  }

  sagaMiddleware.run(rootSaga)

  store.history = history

  return store
}
