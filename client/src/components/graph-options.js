const options = {
  chart: {
    animation: true,
    type: 'line',
    backgroundColor: {
      linearGradient: { x1: 0, y1: 0, x2: 1, y2: 1 },
      stops: [[0, '#333333'], [1, '#272727']]
    },
    style: {
      fontFamily: "'Roboto', sans-serif"
    }
  },
  xAxis: {
    type: '',
    gridLineColor: '#707073',
    labels: {
      enabled: false,
      style: {
        color: '#E0E0E3'
      }
    },
    lineColor: '#707073',
    minorGridLineColor: '#505053',
    tickColor: '#707073',
    title: {
      style: {
        color: '#A0A0A3'
      }
    }
  },
  yAxis: {
    gridLineColor: '#707073',
    labels: {
      style: {
        color: '#E0E0E3'
      }
    },
    lineColor: '#707073',
    minorGridLineColor: '#505053',
    tickColor: '#707073',
    tickWidth: 1,
    title: {
      text: 'Values',
      style: {
        color: '#A0A0A3',
        fontSize: '12px'
      }
    },
    plotLines: [
      {
        value: 0,
        width: 1
      }
    ]
  },
  title: {
    text: 'Accelerometer',
    style: { color: '#FFF', fontSize: '14px' }
  },
  legend: {
    itemStyle: {
      color: '#E0E0E3'
    },
    itemHoverStyle: {
      color: '#FFF'
    },
    itemHiddenStyle: {
      color: '#606063'
    }
  },
  credits: {
    style: {
      color: '#272727'
    }
  },
  series: [
    {
      name: 'X',
      color: '#37c871',
      data: []
    },
    {
      name: 'Y',
      color: '#fff',
      data: []
    },
    {
      name: 'Z',
      color: '#DE3163',
      data: []
    }
  ]
}

export default options
