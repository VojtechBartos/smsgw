'use strict';

import React from 'react';
import {PieChart, BarChart} from 'react-d3';
import _ from 'lodash';
import moment from 'moment';
import Component from '../components/component.react';
import {getStats, getStatsForMonth, getStatsForWeek} from './actions';


class Stats extends Component {

  componentDidMount() {
    const { application } = this.props;
    const appUUID = (application) ? application.uuid : null;

    getStats(appUUID);
    getStatsForWeek(appUUID);
    getStatsForMonth(appUUID);
  }

  translateAllStatsToGraph(data) {
    const count = _.values(data).reduce((a, b) => a + b);

    return Object.keys(data).map(key => {
      const value = Math.round((data[key]/count)*1000) / 10;

      return {
        label: `${key.toUpperCase()} (${data[key]})`,
        value: value || 0
      };
    });
  }

  translateWeekStatsToGraph(data) {
    return ['sent', 'inbox', 'outbox'].map(field => {
      return {
        name: `${field} messages`,
        values: Object.keys(data).map(date => {
          return {
            x: moment(date).format('dddd'),
            y: data[date][field]
          };
        })
      }
    });
  }

  translateMonthStatsToGraph(data) {
    return ['sent', 'inbox', 'outbox'].map(field => {
      return {
        name: `${field} messages`,
        values: Object.keys(data).map(date => {
          return {
            x: moment(date).format('M.D'),
            y: data[date][field]
          };
        })
      }
    });
  }

  render() {
    const { stats } = this.props;
    const { all, week, month } = stats.toJS();

    return (
      <div id="context">
        <div className="left span-3">
          {this.renderStats(all)}
        </div>
        <div className="left span-3">
          {this.renderStatsForWeek(week)}
        </div>
        <div className="left span-3">
          {this.renderStatsForMonth(month)}
        </div>
      </div>
    );
  }

  renderStats(data) {
    if (getStats.pending || !data)
      return 'Loading all statistics ...';

    return (
      <PieChart className="left"
                data={this.translateAllStatsToGraph(data)}
                width={400}
                height={300}
                radius={100}
                innerRadius={20}
                sectorBorderColor="white"
                title="Messages"/>
    );
  }

  renderStatsForWeek(data) {
    if (getStatsForWeek.pending || !data)
      return 'Loading week statistics ...';

    return (
      <BarChart className="left"
                data={this.translateWeekStatsToGraph(data)}
                width={500}
                height={300}
                fill={'#3182bd'}
                title='Last week' />
    );
  }

  renderStatsForMonth(data) {
    if (getStatsForMonth.pending || !data)
      return 'Loading week statistics ...';

    return (
      <BarChart className="left"
                data={this.translateMonthStatsToGraph(data)}
                width={900}
                height={300}
                xAxisClassName='no-legend'
                fill={'#3182bd'}
                title='Last month' />
    );
  }

}

export default Stats;
