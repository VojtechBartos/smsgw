"use strict";

import React from 'react';
import {List} from 'immutable';
import * as store from '../../../../../stores/tags';
import * as actions from '../../../../../actions/tags';
import {flash} from '../../../../../actions/flashMessages';
import Component from '../../../../../lib/component';
import FlashMessages from '../../../../components/flash-messages';
import Subheader from '../../components/sub-header';
import Spinner from '../../../../components/spinner';
import Form from './form';

class Edit extends Component {

  componentDidMount() {
    actions.get(this.uuid()).catch((err) => {
      flash(err.message);

      this.redirectToList();
    })
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.tagForm;
    if (form.isValid()) {
      actions.update(this.uuid(), form.getData()).then(() => {
        flash('Successfuly saved.');
      });
    }
  }

  redirectToList() {
    this.props.router.replaceWith('tags');
  }

  render() {
    const messages = this.props.flashMessages;
    const tag = store.get(this.uuid());

    if (actions.get.pending || !tag) {
      return <Spinner fullscreen={true} />;
    }

    return (
      <div>
        <Subheader backTitle="Tags" backRoute="tags" router={this.props.router}>
          <h1>{tag.label}</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="tagForm"
                pending={actions.update.pending}
                submitTitle="Edit"
                data={tag} />
        </div>
      </div>
    );
  }

}

Edit.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(List).isRequired
};

export default Edit;
