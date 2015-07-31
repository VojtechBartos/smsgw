'use strict';

import React from 'react';
import Immutable from 'immutable';
import {create} from './actions';
import * as templatesActions from '../templates/actions';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Spinner from '../components/spinner.react';
import Form from './form.react';

class Compose extends Component {

  componentDidMount() {
    templatesActions.getAll();
  }

  onFormSubmit(e) {
    e.preventDefault();

    const form = this.refs.composeForm;
    if (form.isValid())
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
  }

  redirectOnSuccess() {
    this.props.router.transitionTo('outbox');
  }

  render() {
    const { flashMessages } = this.props;

    if (templatesActions.getAll.pending)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <FlashMessages messages={flashMessages} />

        <Form onSubmit={(e) => this.onFormSubmit(e)}
              ref="composeForm"
              pending={create.pending}
              {...this.props} />
      </div>
    );
  }

}

Compose.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired,
  templates: React.PropTypes.instanceOf(Immutable.Map).isRequired
};

export default Compose;
