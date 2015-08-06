'use strict';

import React from 'react';
import {Map, List} from 'immutable';
import {get, update} from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';
import Form from './form.react';

class Edit extends Component {

  componentDidMount() {
    get(this.uuid()).catch((err) => {
      flash(err.message);

      this.redirectToList();
    });
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.userForm;
    if (form.isValid())
      update(this.uuid(), form.getData()).then(() => {
        flash('Successfuly saved.');
      });
  }

  redirectToList() {
    this.props.router.transitionTo('users');
  }

  render() {
    const { flashMessages, users } = this.props;
    const user = users.get(this.uuid());

    if (get.pending || !user)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <Subheader backTitle="Back" router={this.props.router}>
          <h1>{user.firstName} {user.lastName}</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={flashMessages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="userForm"
                pending={update.pending}
                submitTitle="Edit"
                data={user}
                adminVersion={true}
                {...this.props} />
        </div>
      </div>
    );
  }

}

Edit.propTypes = {
  router: React.PropTypes.func,
  users: React.PropTypes.instanceOf(Map).isRequired,
  flashMessages: React.PropTypes.instanceOf(List).isRequired
};

export default Edit;
