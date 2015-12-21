'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Grid, Row, Col, Tooltip, OverlayTrigger} from 'react-bootstrap';
import {Map} from 'immutable';
import {get} from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';
import Application from '../applications/application';

class View extends Component {

  componentDidMount() {
    const { application } = this.props;

    get(this.group(), (application) ? application.uuid : null).catch(err => {
      flash(err.message);

      this.redirectToList();
    });
  }

  group() {
    return this.props.router.getCurrentParams().group;
  }

  redirectToList() {
    this.props.router.transitionTo('outbox');
  }

  render() {
    const outbox = this.props.outbox.get(this.group());

    if (get.pending || !outbox)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <Subheader backTitle="Back" router={this.props.router} />

        <div id="context">
          <Grid fluid={true}>
            <Row>
              <Col md={2}>
                <h4>Message <small>({outbox.multiparts.length} parts)</small></h4>
                {outbox.message}
              </Col>
              <Col md={1}>
                <h4>Contacts <small>({outbox.contacts.length})</small></h4>
                {outbox.contacts.map((contact, i) => {
                  const tooltip = <Tooltip>{contact.phoneNumber}</Tooltip>;
                  return (
                    <OverlayTrigger key={i} placement='right' overlay={tooltip}>
                      <Link to="contact-edit" params={{uuid: contact.uuid}}>
                        {contact.lastName} {contact.firstName}
                      </Link>
                    </OverlayTrigger>
                  );
                })}
                <h4>Not contacts <small>({outbox.phoneNumbers.length})</small></h4>
                {outbox.phoneNumbers.map((phoneNumber, i) => {
                  return <div key={i}>{phoneNumber}</div>;
                })}
              </Col>
              <Col md={1}>
                <h4>Will be send</h4>
                {outbox.send}
              </Col>
            </Row>
          </Grid>
        </div>
      </div>
    );
  }

}

View.propTypes = {
  router: React.PropTypes.func,
  outbox: React.PropTypes.instanceOf(Map).isRequired,
  application: React.PropTypes.instanceOf(Application)
};

export default View;
