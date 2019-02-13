import React, { PureComponent } from 'react'
import { shape, func, bool } from 'prop-types'
import { connect } from 'react-redux'
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import Navbar from '../components/navbar.jsx'
import options from '../components/graph-options'
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

    this.state = {
      options: {
        ...options
      }
    }

    this.props.watchData()
  }

  renderAccelerometerOptions = data => ({
    ...options,
    chart: {
      ...options.chart,
      className: 'Dataviz-graph'
    },
    yAxis: {
      ...options.yAxis,
      min: -1.5,
      max: 1.5
    },
    series: [
      ...options.series.map((serie, index) =>
        index === 0
          ? {
              ...serie,
              data: [...data.accelerometer.map(obj => obj.x)],
              animation: false
            }
          : index === 1
          ? {
              ...serie,
              data: [...data.accelerometer.map(obj => obj.y)],
              animation: false
            }
          : {
              ...serie,
              data: [...data.accelerometer.map(obj => obj.z)],
              animation: false
            }
      )
    ]
  })

  renderGyroscopeOptions = data => ({
    ...options,
    title: {
      text: 'Gyroscope',
      style: { color: '#FFF', fontSize: '14px' }
    },
    chart: {
      ...options.chart,
      className: 'Dataviz-graph'
    },
    yAxis: {
      ...options.yAxis,
      min: -1,
      max: 1
    },
    series: [
      ...options.series.map((serie, index) =>
        index === 0
          ? {
              ...serie,
              name: 'Roll',
              data: [...data.gyroscope.map(obj => obj.roll)],
              animation: false
            }
          : index === 1
          ? {
              ...serie,
              name: 'Pitch',
              data: [...data.gyroscope.map(obj => obj.pitch)],
              animation: false
            }
          : {
              ...serie,
              name: 'Yaw',
              data: [...data.gyroscope.map(obj => obj.yaw)],
              animation: false
            }
      )
    ]
  })

  render() {
    const { connected, data } = this.props

    return (
      <div className="Dataviz">
        <Navbar connected={connected} />

        <section className="Dataviz-wrapper">
          <HighchartsReact
            highcharts={Highcharts}
            updateArgs={[true, true, true]}
            options={this.renderAccelerometerOptions(data)}
          />
        </section>

        <section className="Dataviz-wrapper">
          <HighchartsReact
            highcharts={Highcharts}
            updateArgs={[true, true, true]}
            options={this.renderGyroscopeOptions(data)}
          />
        </section>
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
