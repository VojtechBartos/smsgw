'use strict';

import React from 'react';
import Immutable from 'immutable';
import * as store from './store';
import * as actions from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import Form from './form.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';

class Edit extends Component {

  componentDidMount() {
    actions.get(this.uuid()).catch((err) => {
      flash(err.message);

      this.redirectToList();
    });
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.templateForm;
    if (form.isValid())
      actions.update(this.uuid(), form.getData()).then(() => {
        flash('Successfuly saved.');
      });
  }

  redirectToList() {
    this.props.router.transitionTo('templates');
  }

  render() {
    const messages = this.props.flashMessages;
    const template = store.get(this.uuid());

    if (actions.get.pending || !template)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <Subheader backTitle="Templates" router={this.props.router}>
          <h1>{template.label}</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={e => this.onFormSubmit(e)}
                ref="templateForm"
                pending={actions.update.pending}
                submitTitle="Edit"
                data={template} />
        </div>
      </div>
    );
  }

}

Edit.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default Edit;
