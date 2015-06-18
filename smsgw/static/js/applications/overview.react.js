"use strict";

import React from 'react';
import {PieChart, BarChart, AreaChart} from 'react-d3';
import Component from '../components/component.react';

class Overview extends Component {

  constructor(props) {
    super(props);
    this.state = {
      messages: [
        { label: 'Received (120)', value: 60 },
        { label: 'Sent (80)', value: 40 }
      ],
      answers: [
        { label: 'A', value: 5 },
        { label: 'B', value: 6 },
        { label: 'C', value: 20 },
        { label: 'D', value: 15 },
        { label: 'E', value: 10 },
        { label: 'F', value: 7 }
      ]
    };
  }

  render() {
    return (
      <div id="context">
        <div className="left span-3">
          <PieChart className="left"
                    data={this.state.messages}
                    width={400}
                    height={250}
                    radius={100}
                    innerRadius={20}
                    title="Messages" />
        </div>
        <div className="left span-3">
          <BarChart className="left"
                    data={this.state.answers}
                    width={500}
                    height={250}
                    fill={'#3182bd'}
                    title='Answers' />
        </div>
        <div className="left span-3">
          <BarChart className="left"
                    data={this.state.answers}
                    width={500}
                    height={250}
                    fill={'#3182bd'}
                    title='Answers' />
        </div>
      </div>
    );
  }

}

export default Overview;