/* eslint-disable */
'use strict';

const BASE = '/api/1.0';

/**
 * Users resource
 * @type {Object}
 */
export var users = {
  me: () => `${BASE}/users/@me/`,
  signIn: () => `${BASE}/auth/login/`,
  index: () => `${BASE}/users/`,
  create: () => `${BASE}/users/`,
  get: uuid => `${BASE}/users/${uuid}/`,
  resetPassword: uuid => `${BASE}/users/reset-password/${uuid}/`,
  update: uuid => `${BASE}/users/${uuid}/`,
  delete: uuid => `${BASE}/users/${uuid}/`
};

/**
 * Contacts resource
 * @type {Object}
 */
export var contacts = {
  index: (user = "@me") => `${BASE}/users/${user}/contacts/`,
  create: (user = "@me") => `${BASE}/users/${user}/contacts/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/contacts/${uuid}/`,
  update: (uuid, user = "@me") => `${BASE}/users/${user}/contacts/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/contacts/${uuid}/`
};

/**
 * Templates resource
 * @type {Object}
 */
export var templates = {
  index: (user = "@me") => `${BASE}/users/${user}/templates/`,
  create: (user = "@me") => `${BASE}/users/${user}/templates/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/templates/${uuid}/`,
  update: (uuid, user = "@me") => `${BASE}/users/${user}/templates/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/templates/${uuid}/`
};

/**
 * Tags resource
 * @type {Object}
 */
export var tags = {
  index: (user = "@me") => `${BASE}/users/${user}/tags/`,
  create: (user = "@me") => `${BASE}/users/${user}/tags/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/tags/${uuid}/`,
  update: (uuid, user = "@me") => `${BASE}/users/${user}/tags/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/tags/${uuid}/`
};

/**
 * Applications resource
 * @type {Object}
 */
export var applications = {
  index: (user = "@me") => `${BASE}/users/${user}/applications/`,
  create: (user = "@me") => `${BASE}/users/${user}/applications/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/applications/${uuid}/`,
  regenerate: (uuid, user = "@me") => {
    return `${BASE}/users/${user}/applications/${uuid}/regenerate/`;
  },
  update: (uuid, user = "@me") => `${BASE}/users/${user}/applications/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/applications/${uuid}/`
};

/**
 * Outbox resource
 * @type {Object}
 */
export var outbox = {
  validate: () => `${BASE}/outbox/validate/`,
  index: (user = "@me") => `${BASE}/users/${user}/outbox/`,
  create: (user = "@me") => `${BASE}/users/${user}/outbox/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/outbox/${uuid}/`,
  update: (uuid, user = "@me") => `${BASE}/users/${user}/outbox/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/outbox/${uuid}/`
};

/**
 * Sent resource
 * @type {Object}
 */
export var sent = {
  index: (user = "@me") => `${BASE}/users/${user}/sent/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/sent/${uuid}/`,
  delete: (uuid, user = "@me") => `${BASE}/users/${user}/sent/${uuid}/`
};

/**
 * Phones resource
 * @type {Object}
 */
export var phones = {
  index: () => `${BASE}/phones/`
};

/**
 * Inbox resource
 * @type {Object}
 */
export var inbox = {
  index: (user = '@me', application = null) => {
    if (user && application)
      return `${BASE}/users/${user}/applications/${application}/inbox/`;
    else if (user)
      return `${BASE}/users/${user}/inbox/`;
    else
      return `${BASE}/inbox/`;
  },
  delete: (uuid, application = null, user = '@me') => {
    if (user && application)
      return `${BASE}/users/${user}/applications/${application}/inbox/${uuid}/`;
    else if (user)
      return `${BASE}/users/${user}/inbox/${uuid}`;
    else
      return `${BASE}/inbox/${uuid}`;
  }
};
