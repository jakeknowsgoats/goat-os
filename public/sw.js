/* GOAT OS service worker — shows push alerts and opens the STORE LINK on tap. */
self.addEventListener("push", (event) => {
  let d = {};
  try {
    d = event.data ? event.data.json() : {};
  } catch (e) {
    d = {};
  }
  const title = d.title || "🐐 GOAT drop";
  event.waitUntil(
    self.registration.showNotification(title, {
      body: d.body || "",
      tag: d.tag,
      data: { url: d.url || "/" },
      requireInteraction: false,
    })
  );
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = (event.notification.data && event.notification.data.url) || "/";
  // Open the store link directly — no Discord, no extra clicks.
  event.waitUntil(self.clients.openWindow(url));
});
