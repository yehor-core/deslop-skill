import moment from 'moment';

export function Timestamp({ date }: { date: Date }) {
  return <span>{moment(date).format('YYYY-MM-DD')}</span>;
}
