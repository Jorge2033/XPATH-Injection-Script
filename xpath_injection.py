#!/usr/bin/env python3
"""Simple educational XPath injection demo."""

from __future__ import annotations

import argparse
from lxml import etree

USERS_XML = """<users>
  <user><username>admin</username><password>admin123</password><role>admin</role></user>
  <user><username>alice</username><password>alice123</password><role>user</role></user>
  <user><username>bob</username><password>bob123</password><role>user</role></user>
</users>"""


def load_users() -> etree._Element:
    return etree.fromstring(USERS_XML.encode("utf-8"))


def vulnerable_login(username: str, password: str) -> bool:
    root = load_users()
    query = (
        f"//user[username/text()='{username}' and password/text()='{password}']"
    )
    print(f"[VULNERABLE] XPath query: {query}")
    return bool(root.xpath(query))


def safe_login(username: str, password: str) -> bool:
    root = load_users()
    query = "//user[username/text()=$username and password/text()=$password]"
    print(f"[SAFE] XPath query template: {query}")
    return bool(root.xpath(query, username=username, **{"password": password}))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Demonstrate XPath injection against an XML-based login check."
    )
    parser.add_argument("--username", required=True, help="Username input")
    parser.add_argument("--password", required=True, help="Password input")
    parser.add_argument(
        "--safe",
        action="store_true",
        help="Use parameterized XPath (safe mode) instead of vulnerable string concatenation",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.safe:
        success = safe_login(args.username, args.password)
        mode = "SAFE"
    else:
        success = vulnerable_login(args.username, args.password)
        mode = "VULNERABLE"

    if success:
        print(f"[{mode}] Authentication succeeded")
        return 0

    print(f"[{mode}] Authentication failed")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
