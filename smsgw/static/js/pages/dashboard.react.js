'use strict';

import React from 'react';
import {PieChart, BarChart} from 'react-d3';
import Component from '../components/component.react';

class Dashboard extends Component {

  constructor(props) {
    super(props);

    this.state = {
      messages: [
        { label: 'Inbox (1034)', value: 10.8 },
        { label: 'Sent (9510)', value: 89.2 }
      ],
      lastWeek: [
        { label: 'Monday', value: 5 },
        { label: 'Tuesday', value: 6 },
        { label: 'Wednesday', value: 20 },
        { label: 'Thursday', value: 15 },
        { label: 'Friday', value: 10 },
        { label: 'Saturday', value: 10 },
        { label: 'Sunday', value: 7 }
      ],
      lastMonth: Array.from(Array(100).keys()).map(() => {
        return {
          value: Math.floor((Math.random() * 190) + 1)
        };
      })
    };
  }

  render() {
    return (
      <div id="context">
        <div className="left span-3">
          <PieChart className="left"
                    data={this.state.messages}
                    width={400}
                    height={300}
                    radius={100}
                    innerRadius={20}
                    title="Messages" />
        </div>
        <div className="left span-3">
          <BarChart className="left"
                    data={this.state.lastWeek}
                    width={500}
                    height={300}
                    fill={'#3182bd'}
                    title='Last week' />
        </div>
        <div className="left span-3">
          <BarChart className="left"
                    data={this.state.lastMonth}
                    width={900}
                    height={300}
                    fill={'#3182bd'}
                    title='Last month' />
        </div>
      </div>
    );
  }

}

export default Dashboard;
