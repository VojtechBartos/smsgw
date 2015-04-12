'use strict';

let BASE = '/api/1.0';

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
  update: uuid => this.get(uuid),
  delete: uuid => this.get(uuid)
};

/**
 * Contacts resource
 * @type {Object}
 */
export var contacts = {
  index: (user = "@me") => `${BASE}/users/${user}/contacts/`,
  create: (user = "@me") => `${BASE}/users/${user}/contacts/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/contacts/${uuid}/`,
  update: (uuid, user = "@me") => this.get(uuid, user),
  delete: (uuid, user = "@me") => this.get(uuid, user)
};

/**
 * Templates resource
 * @type {Object}
 */
export var templates = {
  index: (user = "@me") => `${BASE}/users/${user}/templates/`,
  create: (user = "@me") => `${BASE}/users/${user}/templates/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/templates/${uuid}/`,
  update: (uuid, user = "@me") => this.get(uuid, user),
  delete: (uuid, user = "@me") => this.get(uuid, user)
};

/**
 * Tags resource
 * @type {Object}
 */
export var tags = {
  index: (user = "@me") => `${BASE}/users/${user}/tags/`,
  create: (user = "@me") => `${BASE}/users/${user}/tags/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/tags/${uuid}/`,
  update: (uuid, user = "@me") => this.get(uuid, user),
  delete: (uuid, user = "@me") => this.get(uuid, user)
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
    return `${BASE}/users/${user}/applications/${uuid}/regenerate/`
  },
  update: (uuid, user = "@me") => this.get(uuid, user),
  delete: (uuid, user = "@me") => this.get(uuid, user)
};

/**
 * Outbox resource
 * @type {Object}
 */
export var outbox = {
  index: (user = "@me") => `${BASE}/users/${user}/outbox/`,
  get: (uuid, user = "@me") => `${BASE}/users/${user}/outbox/${uuid}/`,
  update: (uuid, user = "@me") => this.get(uuid, user),
  delete: (uuid, user = "@me") => this.get(uuid, user)
};
