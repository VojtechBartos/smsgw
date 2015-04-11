'use strict';

import React from 'react';
import Router from 'react-router';
import Routes from './routes';

Router
  .create({ routes: Routes })
  .run(Handler => {
    React.render(<Handler />, document.getElementById('smsgw'))
  })
