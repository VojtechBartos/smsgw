'use strict';

import {Record} from 'immutable';

const TemplateRecord = Record({
  uuid: null,
  label: null,
  text: null,
  createdAt: null
});

export default class Template extends TemplateRecord {}
