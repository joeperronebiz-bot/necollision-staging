/* NEC conversion tracker. OFF by default. No cookies, no storage, no network calls until a provider is wired in.
   Events: call_tap, carwise_click, chat_open, chat_path, chat_lead_sms, chat_lead_email, directions_tap, facebook_click, reviews_click
   Debug: add ?track=debug to any URL to log every event to the browser console.
   To turn on at launch: set ENABLED = true and fill in send() for ONE provider (see LAUNCH.md). */
(function(){
  var ENABLED = false;
  var DEBUG = /[?&]track=debug\b/.test(location.search);
  function send(name, data){
    /* Provider hook. Examples (all commented out until Joe picks one and an account exists):
       GoatCounter:  if (window.goatcounter && goatcounter.count) goatcounter.count({path: 'event/' + name, title: name, event: true});
       Cloudflare Web Analytics: page views only; custom events are not supported, so use GoatCounter or GA4 for these.
       GA4:          if (window.gtag) gtag('event', name, data || {}); */
  }
  function track(name, data){
    if (DEBUG && window.console) console.log('[NEC track]', name, JSON.stringify(data || {}));
    if (ENABLED) { try { send(name, data || {}); } catch(e){} }
  }
  window.NECtrack = track;
  document.addEventListener('click', function(e){
    var a = e.target.closest ? e.target.closest('a') : null;
    if (!a) return;
    var h = a.getAttribute('href') || '';
    var where = a.getAttribute('data-where') || '';
    if (h.indexOf('tel:+12033896400') === 0) track('call_tap', {where: where});
    else if (h.indexOf('carwise.com') > -1) track('carwise_click', {where: where});
    else if (h.indexOf('g.page') > -1 || where === 'reviews') track('reviews_click', {where: where});
    else if (h.indexOf('google.com/maps') > -1) track('directions_tap', {where: where});
    else if (h.indexOf('facebook.com') > -1) track('facebook_click', {where: where});
  }, true);
})();
