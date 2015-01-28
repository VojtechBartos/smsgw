###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
# components
d3 = require 'react-d3'

module.exports = React.createClass

    getInitialState: ->
        messages: [
            { label: 'Received (120)', value: 60 },
            { label: 'Sent (80)', value: 40 }
        ]
        answers: [
            {label: 'A', value: 5} ,
            {label: 'B', value: 6} ,
            {label: 'C', value: 20} ,
            {label: 'D', value: 15} ,
            {label: 'E', value: 10} ,
            {label: 'F', value: 7}
        ]
        traffic: []

    componentDidMount: ->
        traffic = []
        time = new Date().getTime()
        for i in [0..200]
            traffic.push 
                date: time - i * 1500
                value: Math.random() * 1000

        @setState traffic: traffic

    render: ->
        <div id="context">
            <div className="left span-3">
                <d3.PieChart
                    className="left"
                    data={@state.messages}
                    width={400}
                    height={250}
                    radius={100}
                    innerRadius={20}
                    title="Messages" />
            </div>
            <div className="left span-3">
                <d3.BarChart
                    className="left"
                    data={@state.answers}
                    width={500}
                    height={250}
                    fill={'#3182bd'}
                    title='Answers' />
            </div>
            <div className="left span-3">
                <d3.AreaChart
                    data={@state.traffic}
                    width={400}
                    height={250}
                    yAxisTickCount={4}
                    xAxisTickInterval={{unit: "day", interval: 14}}
                    title="Traffic" />
            </div>
        </div>