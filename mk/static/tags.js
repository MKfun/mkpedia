class draft extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }
    connectedCallback() {
        const title = this.getAttribute('title') || 'Default';
        const content = this.getAttribute('content') || '';
        console.log('what');
        this.innerHTML = `
        <div style="align-items:center; display:flex; box-sizing: border-box; gap:1em; font-size: 12px; background: linear-gradient(90deg, rgb(0, 127, 242,.07) 0%, transparent 100%); border-left: 2px solid rgb(0, 127, 242); padding-left: 1em; padding-block:.2em; margin-block:6px;"><div style="user-select:none;"><img alt="Icon-under construction-blue.png" src="/static/32px-Icon-under_construction-blue.png" decoding="async" width="32" height="27" srcset="/w/images/thumb/1/1d/Icon-under_construction-blue.png/48px-Icon-under_construction-blue.png 1.5x, /w/images/thumb/1/1d/Icon-under_construction-blue.png/64px-Icon-under_construction-blue.png 2x" data-file-width="1229" data-file-height="1024"></div><div style="flex:1;"><strong> Эта статья - не доделана. Приветствуется любая помощь </strong> <br>
        <small> <i> Не забудьте согласовать эту статью с причастными статье/упоминаемыми в статье людьми.</i> </small></div>
        </div>
        `;
    }
}
class stub extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }
    connectedCallback() {
        const title = this.getAttribute('title') || 'Default';
        const content = this.getAttribute('content') || '';
        console.log('what');
        this.innerHTML = `
        <div align="left" style="background:#262626; border-radius:.5em; margin:.4em 0; direction:ltr"><div style="display:flex; border:1px solid rgb(38,139,255,.3); border-radius:.2em; overflow:hidden">
        <p style="background:rgb(38,139,255,.3); align-items:center; display:flex; margin:0; padding:.3em; padding-inline:.75em; justify-content:center; font-weight:bold">Пусто</p>
        <p style="background:rgb(38,139,255,.1); box-shadow:rgb(38,139,255,.05) 0 0 25px 0 inset; flex:1; margin:0; padding:.3em; text-align:left">
        Эта статья - пустышка. Вы можете помочь дописав ее.
        </p>
        </div></div>
        `;
    }
}
class cleanup extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }
    connectedCallback() {
        const title = this.getAttribute('title') || 'Default';
        const content = this.getAttribute('content') || '';
        console.log('what');
        this.innerHTML = `
        <div style="align-items:center; display:flex; box-sizing: border-box; gap:1em; font-size: 12px; background: linear-gradient(90deg, rgb(244, 196, 48,.07) 0%, transparent 100%); border-left: 2px solid rgb(244, 196, 48); padding-left: 1em; padding-block:.2em; margin-block:6px;"><div style="user-select:none;"><img alt="Broom icon.png" src="/static/32px-Icon-broom.png" decoding="async" width="32" height="32" srcset="/w/images/thumb/7/71/Icon-broom.png/48px-Icon-broom.png 1.5x, /w/images/thumb/7/71/Icon-broom.png/64px-Icon-broom.png 2x" data-file-width="400" data-file-height="400"></div><div style="flex:1;"><b>Эту статью или раздел необходимо привести в соответствие с более высоким стандартом качества</b>.<br><small><i><a href="http://en.wikipedia.org/wiki/Wikipedia:Cleanup_process#Advice_on_fixing_articles" class="extiw" title="wikipedia:Wikipedia:Cleanup process"> Wikipedia cleanup process</a> в помощь. Так же, не забудьте согласовать эту статью с причастными статье/упоминаемыми в статье людьми</a>.</i></small></div>
        </div>
        `;
    }
}
class wikiwarning extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }
    connectedCallback() {
        const title = this.getAttribute('title') || 'Default';
        const content = this.getAttribute('content') || '';
        console.log('what');
        setTimeout(() => this.innerHTML = `
        <div style="margin:.5em 0; margin-left:calc(2em * 0); display:flex; gap:4px;background:linear-gradient(90deg, rgba(255,32,32,.04) 0%, transparent 100%); border-left:2px solid rgb(255,32,32); border-radius:2px; padding:6px 0 4px 12px;"><strong style="display:table-cell; color:rgb(255,32,32); white-space:nowrap;"><span style="user-select:none;"><span style="margin-right:4px;"><img alt="Warning.png" src="/static/10px-Warning.png" decoding="async" width="10" height="12" data-file-width="500" data-file-height="600"></span></span>Предупреждение:</strong><span style="display:table-cell;">` + content +`</span></div>
        `);
    }
}
class wikiconfirm extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }
    connectedCallback() {
        const title = this.getAttribute('title') || 'Default';
        const content = this.getAttribute('content') || '';
        console.log('what');
        setTimeout(() => this.innerHTML = `
        <div style="margin:0.4em 1em 0.5em;"><strong style="color:#8BC53F; display:table-cell; text-align:right; white-space:nowrap; padding-right:0.3em;"><img alt="" src="/static/10px-Confirm.png" decoding="async" width="10" height="13" data-file-width="500" data-file-height="650"> Подтвердить:</strong><span style="display:table-cell;">` + content + `</span></div>
        `);
    }
}
customElements.define("wiki-draft", draft);
customElements.define("wiki-stub", stub);
customElements.define("wiki-cleanup", cleanup);
customElements.define("wiki-warning", wikiwarning);
customElements.define("wiki-confirm", wikiconfirm);
