# AutoKey config

## Requirements

These scripts have been rewritten to work with the "[autokey-py3][akpy3]"
version of [AutoKey][wp], which means Python 3.<sup>\*</sup>

I installed this version of AutoKey with `pip3 install autokey` rather than
using the distro-supplied version, or a PPA, because of problems I had with the
[clipboard functions][clip] on newer distros, namely elementaryOS Loki, based
on Ubuntu 16.04 (Xenial).

<sup>\*</sup>_There's an abandoned copy of my old Python 2.x-compatible AutoKey
config at [ernstki/autokey-config-py27][akcpy27]_


## How to use this

When you're setting up a new system, you can clone this repository to
`~/.config/autokey`:

```bash
cd ~/.config
test -f autokey && mv autokey autokey.old

# Weirauch Lab (internal)
git clone $GITHOSTURL/$MYUSER/autokey-config.git autokey

# GitHub
git clone https://github.com/ernstki/autokey-config autokey
```

Then you should be able to just fire up AutoKey from the system menus.


# Scripting reference
The AutoKey project's documentation got a little bit disorganized when the
original maintainer stopped, um, maintaining it. Now there are two GitHub
projects, and the original [Google Code site][gc] which is basically just a
tombstone.

Here are some essential references can be kind of hard to find:

* [AutoKey API Documentation][api] - _original API reference_
* [Special Keys][keys] - _on the [GitHub wiki][wiki]_


## See also

* [autokey-users][gg] Google Group


## License

Made available under the terms of version 2 of the [WTFPL][].


[akpy3]: https://github.com/autokey-py3/autokey
[wp]: https://en.wikipedia.org/wiki/AutoKey
[clip]: https://autokey-py3.github.io/lib.scripting.GtkClipboard-class.html
[akcpy27]: https://github.com/ernstki/autokey-config-py27
[gc]: https://code.google.com/archive/p/autokey/
[api]: https://autokey-py3.github.io/index.html
[keys]: https://github.com/autokey-py3/autokey/wiki/Special-Keys
[gg]: https://groups.google.com/forum/#!forum/autokey-users
[wiki]: https://github.com/autokey-py3/autokey/wiki
[wtfpl]: http://www.wtfpl.net/txt/copying/
