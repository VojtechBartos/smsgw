'use strict';

import React from 'react';
import Router from 'react-router';
import routes from './routes';

const element = document.getElementById('smsgw');

Router.run(routes, (Handler) => {
  console.time('app render on route change'); // eslint-disable-line no-console
  React.render(<Handler />, element, () => {
    console.timeEnd('app render on route change'); // eslint-disable-line no-console
  });
});
