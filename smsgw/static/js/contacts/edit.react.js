'use strict';

import React from 'react';
import Immutable from 'immutable';
import * as store from './store';
import * as actions from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';
import Form from './form.react';

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
    const form = this.refs.contactForm;
    if (form.isValid())
      actions.update(this.uuid(), form.getData()).then(() => {
        flash('Successfuly saved.');
      });
  }

  redirectToList() {
    this.props.router.transitionTo('contacts');
  }

  render() {
    const messages = this.props.flashMessages;
    const contact = store.get(this.uuid());

    if (actions.get.pending || !contact)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <Subheader backTitle="Contacts" router={this.props.router}>
          <h1>{contact.firstName} {contact.lastName}</h1>
          <h2>{contact.phoneNumber}</h2>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="contactForm"
                pending={actions.update.pending}
                submitTitle="Edit"
                data={contact}
                {...this.props} />
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
