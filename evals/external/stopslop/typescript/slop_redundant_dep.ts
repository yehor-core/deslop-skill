import moment from 'moment';
import { v4 as uuidv4 } from 'uuid';
const fetchPolyfill = require('node-fetch');

export function formatDate(date: Date) {
  return moment(date).format('YYYY-MM-DD');
}

export function newId(prefix: string) {
  return `${prefix}-${uuidv4()}`;
}

export function getJson(url: string) {
  console.log('fetching', url);
  return fetchPolyfill(url);
}
