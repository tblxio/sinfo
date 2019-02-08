import React from 'react'
import { Switch, Route } from 'react-router-dom'
import DataViz from './containers/data-viz.jsx'

const routes = [
  {
    path: '/',
    component: DataViz,
    exact: true
  }
]

const AppRoot = () => (
  <Route
    render={({ location }) => (
      <Switch location={location}>
        {routes.map((route, index) => (
          <Route
            {...route}
            key={index.toString()}
            path={typeof route.path === 'function' ? route.path() : route.path}
          />
        ))}
      </Switch>
    )}
  />
)

export default AppRoot
