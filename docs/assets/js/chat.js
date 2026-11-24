/* NEC chat helper. Scripted buttons only. No AI, no third-party widget, no network calls.
   Details live in memory only (no cookies, no localStorage) and leave the page only when the
   visitor presses send in their own app (Message Us, off until texting is confirmed). */
(function(){
  var PHONE='tel:+12033896400', PHONE_TXT='(203) 389-6400';
  var SMS='sms:+12033896400';                 /* [CONFIRM] can (203) 389-6400 receive text messages? */
  var SMS_ON=false;  /* Mirror fix 6: Message Us send stays off until Phones & Admin confirms (203) 389-6400 takes texts */
  var CARWISE='https://www.carwise.com/online-photo-estimate/new-england-collision-west-haven-ct-06516/462487';
  var LAW1='You have the right to choose the licensed repair shop where the damage to your motor vehicle will be repaired.';
  var LAW2='Your insurance company cannot require you to use a specific repair shop.';
  var t=window.NECtrack||function(){};
  var d={}, opener=null, panel, log, opts, live;
  var PATHS={
    accident:'Accident just happened',
    towyard:'My car is at a tow yard',
    claim:'I have an attorney or claim question',
    photos:'Get a photo estimate'
  };
  function el(tag,attrs,html){var e=document.createElement(tag);for(var k in attrs){e.setAttribute(k,attrs[k]);}if(html!=null)e.innerHTML=html;return e;}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function say(html,me){var m=el('div',{'class':'msg'+(me?' me':'')},html);log.appendChild(m);log.scrollTop=log.scrollHeight;}
  function clear(){opts.innerHTML='';}
  function focusFirst(){var f=opts.querySelector('input,textarea,button,a');if(f)f.focus();}
  function choices(list){
    clear();
    list.forEach(function(c){
      var b;
      if(c.href){b=el('a',{'class':'btn '+(c.cls||'btn-soft'),href:c.href,'data-where':'chat'},c.label);if(c.ext){b.target='_blank';b.rel='noopener';}if(c.on)b.addEventListener('click',c.on);}
      else{b=el('button',{type:'button','class':'btn '+(c.cls||'btn-soft')},c.label);b.addEventListener('click',function(){say(esc(c.label),true);c.go();});}
      opts.appendChild(b);
    });
    focusFirst();
  }
  function ask(q,fields,next,skip){
    say(q);clear();
    var f=el('form',{'class':'chat-form',novalidate:'novalidate'});
    fields.forEach(function(x){
      var id='nec-'+x.k;
      f.appendChild(el('label',{'for':id},x.label));
      var i=el(x.area?'textarea':'input',x.area?{id:id,name:x.k,rows:'3'}:{id:id,name:x.k,type:x.type||'text',autocomplete:x.ac||'off',inputmode:x.im||'text'});
      if(x.ph)i.setAttribute('placeholder',x.ph);
      f.appendChild(i);
    });
    var err=el('p',{'class':'err',role:'alert'},'');f.appendChild(err);
    f.appendChild(el('button',{type:'submit','class':'btn btn-call'},'Next'));
    if(skip){var s=el('button',{type:'button','class':'btn btn-soft'},skip);s.addEventListener('click',function(){fields.forEach(function(x){d[x.k]='Not sure';});say(esc(skip),true);next();});f.appendChild(s);}
    f.addEventListener('submit',function(e){
      e.preventDefault();var ok=true,shown=[];
      fields.forEach(function(x){var v=f.elements[x.k].value.trim();if(!v&&!x.opt)ok=false;d[x.k]=v;if(v)shown.push(v);});
      if(x_phone_bad(fields)){err.textContent='Please check the phone number, so we can reach you.';return;}
      if(!ok){err.textContent='Please fill this in, or tap Call if that is easier.';return;}
      say(esc(shown.join(' ')),true);next();
    });
    opts.appendChild(f);focusFirst();
  }
  function x_phone_bad(fields){for(var i=0;i<fields.length;i++){if(fields[i].k==='phone'){var n=(d.phone||'').replace(/\D/g,'');return n.length<10;}}return false;}
  /* ---- flow ---- */
  function start(){
    log.innerHTML='';d={};
    say('Hi, this is New England Collision\u2019s quick help. Tap an answer below, and a real person from our shop follows up. First, is everyone okay? If anyone is hurt, please call 911.');
    choices([{label:'Everyone is okay',cls:'btn-call',go:help},{label:'Someone is hurt',go:hurt}]);
  }
  function hurt(){
    say('Please call 911 now. People come first. When you are ready, we are here to help with the car.');
    choices([{label:'Call 911',href:'tel:911',cls:'btn-call'},{label:'I am okay to keep going',go:help}]);
  }
  function help(){
    say('We are glad you are okay. Take a breath. We can help from here. What would help most right now?');
    choices(Object.keys(PATHS).map(function(k){return{label:PATHS[k],go:function(){d.path=PATHS[k];t('chat_path',{path:k});path(k);}};}));
  }
  function path(k){
    if(k==='accident'){
      say('We are sorry this happened. Nobody plans an accident. If your car cannot be driven: we do not tow, but we know trusted local tow companies and can call them for you.');
      say('In Connecticut, the choice of repair shop is yours. <span class="law">'+LAW1+'</span>');
    }else if(k==='towyard'){
      say('That can feel stressful, and you do not have to sort it out alone. Every situation is different, so call us and we will help you sort it out.');
      say('<span class="law">'+LAW1+'</span>');
    }else if(k==='claim'){
      say('We are a repair shop, so we cannot give legal advice. For legal questions, please ask your attorney. We can help with the repair side of things. We accept Letters of Protection from attorneys. Call us and we will help you sort it out.');
      say('<span class="law">'+LAW2+'</span>');
    }else{
      say('You can send photos of the damage from your phone through CarWise, and our shop looks them over. First, a few quick details so we know who you are.');
      return details();
    }
    say('Would you like someone from our shop to follow up with you? It takes about a minute.');
    choices([{label:'Yes, please follow up',cls:'btn-call',go:details},{label:'Call '+PHONE_TXT,href:PHONE}]);
  }
  function details(){
    say('<span class="privacy">This page doesn\u2019t save what you type. It reaches our shop only when you press send in your own messages app. We use it only to help with your repair, and we never sell it.</span>');
    ask('What is your name?',[{k:'name',label:'Your name',ac:'name'}],function(){
      ask('Thanks, '+esc(d.name)+'. What is the best phone number to reach you?',[{k:'phone',label:'Phone number',type:'tel',ac:'tel',im:'tel'}],function(){
        ask('What are you driving?',[{k:'year',label:'Year',im:'numeric',ph:'2019'},{k:'make',label:'Make',ph:'Honda'},{k:'model',label:'Model',ph:'CR-V'}],function(){
          ask('In a few words, what happened?',[{k:'what',label:'What happened',area:true,ph:'Rear-ended at a light, bumper and trunk damage'}],function(){
            ask('Who is your insurance company? It can be yours or the other driver\u2019s.',[{k:'ins',label:'Insurance company'}],handoff,'Not sure yet');
          });
        });
      });
    });
  }
  function body(){
    return 'Hi New England Collision, this is '+d.name+'. Phone: '+d.phone+'. Vehicle: '+[d.year,d.make,d.model].join(' ')+'. What happened: '+d.what+'. Insurance: '+d.ins+'. I chose: '+(d.path||'')+'. (From the necollision.com chat helper)';
  }
  function handoff(){
    var b=body();
    say('Thank you, '+esc(d.name)+'. Here is what you told us:<br><br>'+esc(b));
    say('To reach us now, tap Call. A real person at our shop answers during business hours.');
    say('You can also send photos of the damage on CarWise. We are open Mon to Fri, 8:00 AM to 4:30 PM.');
    clear();
    var list=[
      {label:'Call '+PHONE_TXT,href:PHONE,cls:'btn-call'},
      {label:'Send photos on CarWise',href:CARWISE,ext:true}
    ];
    if(SMS_ON) list.push({label:'Message Us',href:SMS+'?&body='+encodeURIComponent(b),on:function(){t('chat_lead_sms',{path:d.path});}});
    choices(list);
    var again=el('button',{type:'button','class':'btn btn-ghost'},'Start over');again.addEventListener('click',start);opts.appendChild(again);
  }
  /* ---- panel ---- */
  function build(){
    panel=el('div',{'class':'chat',id:'nec-chat',role:'dialog','aria-modal':'false','aria-labelledby':'nec-chat-title',hidden:''});
    var base=document.documentElement.getAttribute('data-base')||'';
    panel.innerHTML='<div class="chat-h"><img src="'+base+'assets/img/nec-logo-160.webp" alt="" width="36" height="36"><b id="nec-chat-title">New England Collision<small>Here to help</small></b><button type="button" class="chat-x" aria-label="Close chat">\u00d7</button></div>'+
      '<div class="chat-log" aria-live="polite"></div><div class="chat-opts"></div>'+
      '<div class="chat-foot"><span>Rather talk?</span><a href="'+PHONE+'" data-where="chat-footer">Call '+PHONE_TXT+'</a></div>';
    document.body.appendChild(panel);
    log=panel.querySelector('.chat-log');opts=panel.querySelector('.chat-opts');
    panel.querySelector('.chat-x').addEventListener('click',close);
    panel.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  }
  function open(e){
    if(e)e.preventDefault();
    if(!panel)build();
    opener=document.activeElement;
    if(panel.hidden){panel.hidden=false;t('chat_open',{from:(opener&&opener.getAttribute('data-where'))||''});if(!log.children.length)start();else focusFirst();}
  }
  function close(){panel.hidden=true;if(opener&&opener.focus)opener.focus();}
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-chat]');if(a)open(e);});
  window.NECchat={open:open,close:close};
})();
