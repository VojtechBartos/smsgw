'use strict';

import React from 'react';
import {PieChart, BarChart} from 'react-d3';
import Component from '../components/component.react';

class Overview extends Component {

  constructor(props) {
    super(props);
    this.state = {
      messages: [
        { label: 'Inbox (120)', value: 60 },
        { label: 'Sent (80)', value: 40 }
      ],
      stats: [
        { label: 'Monday', value: 5 },
        { label: 'Tuesday', value: 6 },
        { label: 'Wednesday', value: 20 },
        { label: 'Thursday', value: 15 },
        { label: 'Friday', value: 10 },
        { label: 'Saturday', value: 10 },
        { label: 'Sunday', value: 7 }
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
                    data={this.state.stats}
                    width={500}
                    height={250}
                    fill={'#3182bd'}
                    title='Last week' />
        </div>
      </div>
    );
  }

}

export default Overview;
