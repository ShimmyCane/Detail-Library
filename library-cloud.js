// Detail Library: cloud copies, in the same Supabase project as Quick Detail.
// A cloud copy is one row in sketch_details, marked metadata.source = 'detail-library'. The image sits in items[0]
// as a JPEG data URL (the same form Quick Detail uses for an image on a sheet), and a small thumbnail sits in
// metadata.thumb so the list loads quickly.
// Only the owner account can read or write these tables (row level security in the database), so every
// call needs a signed-in session. Loaded after the Supabase script. Exposes window.DLCloud.
(function (root) {
    'use strict';

    var CFG = {
        url: 'https://xabgankckrcuhcgdolrg.supabase.co',
        // Public values, the same ones Quick Detail ships. Row level security protects the data.
        key: 'sb_publishable_kncKodoYJZ6ByexwWM_TtQ_OpW68M5f',
        // Set this to the Quick Detail app's address, so "Open in Quick Detail" opens it in a new tab.
        quickDetailUrl: '',
        source: 'detail-library'
    };

    var client = null;

    function ready() {
        return !!root.supabase;
    }

    function sb() {
        if (client) return client;
        if (!root.supabase) throw new Error('The cloud library did not load. Check the connection and reload.');
        client = root.supabase.createClient(CFG.url, CFG.key, {
            auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true }
        });
        return client;
    }

    function session() {
        return sb().auth.getSession().then(function (r) { return r.data.session; });
    }

    function signIn(email, password) {
        return sb().auth.signInWithPassword({ email: email, password: password }).then(function (r) {
            if (r.error) throw r.error;
            return r.data.session;
        });
    }

    function signOut() {
        return sb().auth.signOut().then(function (r) { if (r && r.error) throw r.error; });
    }

    // A stable row key for one library item, so the same item always maps to the same cloud row.
    function rowIdFor(key) {
        var h = 2166136261;
        for (var i = 0; i < key.length; i++) {
            h ^= key.charCodeAt(i);
            h = Math.imul(h, 16777619) >>> 0;
        }
        return 'dl-' + h.toString(16) + '-' + key.replace(/[^a-z0-9]+/gi, '-').toLowerCase().slice(0, 60);
    }

    // Lists this library's cloud copies, newest first. Items (the full images) are not loaded here.
    function list() {
        return sb().from('sketch_details')
            .select('id, local_id, name, tags, metadata, updated_at')
            .is('deleted_at', null)
            .contains('metadata', { source: CFG.source })
            .order('updated_at', { ascending: false })
            .then(function (r) { if (r.error) throw r.error; return r.data || []; });
    }

    // Loads one copy's full image (the data URL).
    function loadImage(id) {
        return sb().from('sketch_details').select('items').eq('id', id).single()
            .then(function (r) {
                if (r.error) throw r.error;
                var it = (r.data.items || [])[0];
                if (!it || !it.src) throw new Error('This cloud copy has no image.');
                return it.src;
            });
    }

    // Writes (or rewrites) the cloud copy of one item. image: { dataUrl, thumbUrl, width, height }.
    function save(entry, image) {
        var localId = rowIdFor(entry.key);
        var w = 12;                                    // inches on the sheet; the height follows the aspect ratio
        var h = image.height && image.width ? w * image.height / image.width : w;
        var row = {
            local_id: localId,
            name: entry.title,
            scale: 'image',
            tags: entry.tags || [],
            // noPrint: the picture is a background underlay in Quick Detail, under the drawing, and never prints.
            items: [{ id: 'img-1', kind: 'image', src: image.dataUrl, at: [0, 0], w: w, h: h, name: entry.title, noPrint: true }],
            metadata: {
                source: CFG.source,
                path: entry.path || null,
                kind: entry.kind,
                licence: entry.licence || 'unverified',
                credit: entry.credit || '',
                origin_url: entry.source || '',
                thumb: image.thumbUrl,
                rating: 1,
                pixels: [image.width, image.height]
            },
            updated_at: new Date().toISOString()
        };
        return sb().from('sketch_details')
            .upsert(row, { onConflict: 'local_id' })
            .select('id, local_id')
            .single()
            .then(function (r) { if (r.error) throw r.error; return r.data; });
    }

    // Changes the tags on a cloud copy.
    function setTags(id, tags) {
        return sb().from('sketch_details').update({ tags: tags, updated_at: new Date().toISOString() }).eq('id', id)
            .then(function (r) { if (r.error) throw r.error; });
    }

    // Renames a cloud copy.
    function rename(id, name) {
        return sb().from('sketch_details').update({ name: name, updated_at: new Date().toISOString() }).eq('id', id)
            .then(function (r) { if (r.error) throw r.error; });
    }

    root.DLCloud = {
        config: CFG,
        ready: ready,
        session: session,
        signIn: signIn,
        signOut: signOut,
        list: list,
        loadImage: loadImage,
        save: save,
        setTags: setTags,
        rename: rename,
        rowIdFor: rowIdFor
    };
})(typeof window !== 'undefined' ? window : globalThis);
