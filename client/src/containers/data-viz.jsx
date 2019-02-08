import React, { PureComponent } from 'react'
import { shape, func, bool } from 'prop-types'
import { connect } from 'react-redux'
import Navbar from '../components/navbar.jsx'
import { getData, getStatus, watchData } from '../duxs/data-viz'

class DataViz extends PureComponent {
  static propTypes = {
    connected: bool,
    data: shape({}),
    watchData: func
  }

  static defaultProps = {
    connected: false,
    data: {},
    watchData: () => null
  }

  constructor(props) {
    super(props)

    this.props.watchData()
  }

  render() {
    const { connected } = this.props

    return (
      <div>
        <Navbar connected={connected} />
      </div>
    )
  }
}

const mapStateToProps = state => ({
  connected: getStatus(state),
  data: getData(state)
})

const mapDispatchToProps = dispatch => ({
  watchData: () => dispatch(watchData())
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DataViz)
