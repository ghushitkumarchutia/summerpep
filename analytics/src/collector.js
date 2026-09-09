const globalEventHistory = [];

export const trackEvent = (event) => {
  globalEventHistory.push(event);

  const clientVersion = event.client.device.platform.version;
  const trackingId = event.meta.session.id;

  return {
    tracked: true,
    totalBuffered: globalEventHistory.length,
    clientVersion,
    trackingId
  };
};

export const getBufferedEvents = () => {
  return globalEventHistory;
};
