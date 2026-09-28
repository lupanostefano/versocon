# VersoCon — v0.3.4 — Release notes

## 🔒 Security update — CVE-2024-4367 (pdf.js)
- 🛡️ **PDF editor hardened against CVE-2024-4367.** The bundled pdf.js 3.11.174 falls in the affected range (0.8.1181 → 4.1.392, fixed upstream in 4.2.67). Every `getDocument` call now sets `isEvalSupported: false`, which disables the code path that could compile attacker-controlled font data through `Function` — the mitigation recommended by the pdf.js project until the library itself is upgraded.
- ✅ **No behaviour change:** PDF previews, password-protected files, scan cleanup, signing and every other flow work exactly as in v0.3.3.
- 📦 **winget channel is live:** the `HikariHasegawa.VersoCon` package was approved and published — `winget install HikariHasegawa.VersoCon`.

## SHA-256

`versocon-setup-0.3.4.exe`
`<SHA-256 aggiornato a build CI completata>`

(Windows: `Get-FileHash versocon-setup-0.3.4.exe -Algorithm SHA256`).

## 🔒 Is it safe? / È sicuro?

**Yes — VersoCon is 100% local, open-source, with no telemetry and no account.**
It runs entirely on your machine (`127.0.0.1`); nothing ever goes online.

> ### Windows shows "Windows protected your PC" (SmartScreen)
> This is **normal** for unsigned open-source software and does **not** mean VersoCon contains a virus.
> Before you proceed, verify:
>
> 1. **SHA-256** — compare the hash of your downloaded file with the one on this release page
>    (Windows: `Get-FileHash versocon-setup-*.exe -Algorithm SHA256`).
> 2. **VirusTotal** (optional) — upload your copy at
>    [virustotal.com](https://www.virustotal.com/gui/home/url) and check the result.
> 3. **Source code** — the code that built this file is on
>    [github.com/lupanostefano/versocon](https://github.com/lupanostefano/versocon).
>
> If everything checks out, click **More info → Run anyway / Esegui comunque**.
>
> ### Prefer an installer that never asks?
> Install through a package manager:
> ```
> winget install HikariHasegawa.VersoCon    # official Windows package manager (live)
> scoop bucket add HikariHasegawa https://github.com/lupanostefano/bucket
> scoop install versocon                     # Scoop, from the author's bucket above (live)
> ```

<!-- Italiano -->

**Sì — VersoCon è 100% locale, open-source, senza telemetria e senza account.**
Ogni cosa gira sulla tua macchina (`127.0.0.1`); nessun file va mai online.

> ### Windows mostra "Windows ha protetto il tuo PC" (SmartScreen)
> È **normale** per software open-source non firmato e **non** indica la presenza di un virus.
> Prima di procedere, verifica:
>
> 1. **SHA-256** — confronta l'hash del file scaricato con quello della pagina della release
>    (Windows: `Get-FileHash versocon-setup-*.exe -Algorithm SHA256`).
> 2. **VirusTotal** (facoltativo) — carica la tua copia su
>    [virustotal.com](https://www.virustotal.com/gui/home/url) e controlla il risultato.
> 3. **Codice sorgente** — chi ha costruito questo file è su
>    [github.com/lupanostefano/versocon](https://github.com/lupanostefano/versocon).
>
> Se tutto è OK → **Altre informazioni → Esegui comunque**.
>
> ### Preferisci un canale che non chiede nulla?
> Installa con un package manager:
> ```
> winget install HikariHasegawa.VersoCon    # canale Microsoft (ora attivo)
> scoop bucket add HikariHasegawa https://github.com/lupanostefano/bucket
> scoop install versocon                     # Scoop, dal bucket dell'autore qui sopra (già attivo)
> ```

## FAQ

**Q: What changed in v0.3.4?** / **Cosa cambia nella v0.3.4?**
A: A security hardening of the PDF editor against CVE-2024-4367 (see the top of these notes). No other behaviour changed. / Una mitigazione di sicurezza dell'editor PDF per CVE-2024-4367 (vedi inizio delle note). Nessun altro comportamento è cambiato.

**Q: Why does Windows warn me?** / **Perché Windows mi avvisa?**
A: The installer is not digitally signed (a code-signing certificate requires a business entity — see the roadmap). SmartScreen is a generic caution, not a malware report. / Non è firmato con certificato (serve una ditta — vedi roadmap). SmartScreen è una cautela generica, non un report di malware.

**Q: How do I know it's not a virus?** / **Come so che non è un virus?**
A: (1) The source is public on GitHub. (2) The binary you run is built *from* that source in a public GitHub Actions log. (3) SHA-256 and VirusTotal give you 2 independent confirmations. / (1) Il codice è pubblico. (2) Il binario che esegui è costruito *da* quello in una CI GHA pubblica. (3) SHA-256 e VirusTotal danno 2 verifiche indipendenti.

**Q: When will the warning go away?** / **Quando sparisce l'avviso?**
A: For most users within weeks, once SmartScreen has enough "clean install" reports. Definitively, once we get a code-signing certificate (needs a business license). / Per la maggior parte degli utenti in poche settimane. In modo definitivo quando avremo il certificato di firma (richiede una ditta).

**Q: Does v0.3.4 include the security fixes from previous releases?** / **La v0.3.4 include i fix di sicurezza delle versioni precedenti?**
A: Yes — all of them (path traversal, DNS-rebinding/CSRF protection, hidden console windows, Italian translation fixes, editor geometry on rotated pages). / Sì — tutti (path traversal, protezione DNS-rebinding/CSRF, finestre console nascoste, fix delle traduzioni italiane, geometria dell'editor su pagine ruotate).
