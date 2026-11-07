// Detail Library: this browser's storage.
// Local copies (images, SVGs and PDFs saved on this device) live in IndexedDB. Names and tags you add to any
// item are kept in localStorage, keyed by item key. Nothing here is shared with other devices.
// Loaded before library.html's script. Exposes window.DLStore.
(function (root) {
    'use strict';

    var DB_NAME = 'detailLibrary';
    var DB_VERSION = 1;
    var STORE = 'copies';
    var NAMES_KEY = 'detailLibrary.names.v1';
    var TAGS_KEY = 'detailLibrary.tags.v1';
    var BG_KEY = 'detailLibrary.bg.v1';

    var ok = { storage: true, idb: true };

    function readJSON(key, fallback) {
        try {
            var raw = root.localStorage.getItem(key);
            var v = raw ? JSON.parse(raw) : fallback;
            return v && typeof v === 'object' ? v : fallback;
        } catch (e) {
            ok.storage = false;
            return fallback;
        }
    }

    function writeJSON(key, value) {
        try {
            root.localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            ok.storage = false;
            return false;
        }
    }

    // ---- Names and tags (localStorage) ----
    var names = readJSON(NAMES_KEY, {});
    var tags = readJSON(TAGS_KEY, {});

    function nameOverride(key) {
        return typeof names[key] === 'string' ? names[key] : null;
    }
    function setName(key, name) {
        if (name) names[key] = name; else delete names[key];
        return writeJSON(NAMES_KEY, names);
    }
    function localTags(key) {
        return Array.isArray(tags[key]) ? tags[key].slice() : [];
    }
    function setLocalTags(key, list) {
        if (list && list.length) tags[key] = list; else delete tags[key];
        return writeJSON(TAGS_KEY, tags);
    }

    // ---- Background choice ----
    function readBg() {
        try {
            var v = root.localStorage.getItem(BG_KEY);
            return v === 'dark' || v === 'mono' ? v : 'sheet';
        } catch (e) {
            ok.storage = false;
            return 'sheet';
        }
    }
    function writeBg(bg) {
        try { root.localStorage.setItem(BG_KEY, bg); } catch (e) { ok.storage = false; }
    }

    // ---- Local copies (IndexedDB) ----
    var dbPromise = null;
    function db() {
        if (dbPromise) return dbPromise;
        dbPromise = new Promise(function (resolve, reject) {
            if (!root.indexedDB) { ok.idb = false; reject(new Error('IndexedDB is not available in this browser.')); return; }
            var req = root.indexedDB.open(DB_NAME, DB_VERSION);
            req.onupgradeneeded = function () {
                var d = req.result;
                if (!d.objectStoreNames.contains(STORE)) d.createObjectStore(STORE, { keyPath: 'id' });
            };
            req.onsuccess = function () { resolve(req.result); };
            req.onerror = function () { ok.idb = false; reject(req.error); };
        });
        return dbPromise;
    }

    function tx(mode, fn) {
        return db().then(function (d) {
            return new Promise(function (resolve, reject) {
                var t = d.transaction(STORE, mode);
                var store = t.objectStore(STORE);
                var result;
                var req = fn(store);
                if (req) req.onsuccess = function () { result = req.result; };
                t.oncomplete = function () { resolve(result); };
                t.onerror = function () { reject(t.error); };
                t.onabort = function () { reject(t.error); };
            });
        });
    }

    // record: { id, name, kind, mime, blob, licence, credit, source, cloudId, created }
    function putCopy(record) {
        return tx('readwrite', function (s) { return s.put(record); }).then(function () { return record; });
    }
    function getCopy(id) {
        return tx('readonly', function (s) { return s.get(id); });
    }
    function allCopies() {
        return tx('readonly', function (s) { return s.getAll(); }).then(function (list) { return list || []; });
    }
    function deleteCopy(id) {
        return tx('readwrite', function (s) { return s.delete(id); });
    }

    root.DLStore = {
        status: ok,
        nameOverride: nameOverride,
        setName: setName,
        localTags: localTags,
        setLocalTags: setLocalTags,
        readBg: readBg,
        writeBg: writeBg,
        putCopy: putCopy,
        getCopy: getCopy,
        allCopies: allCopies,
        deleteCopy: deleteCopy
    };
})(typeof window !== 'undefined' ? window : globalThis);
