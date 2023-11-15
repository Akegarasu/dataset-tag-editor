import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--share",
    action="store_true",
    help="Launch gradio with share=True option and make accessible from internet",
    default=False,
)
parser.add_argument(
    "--port", type=int, help="Launch gradio with given port number", default=None
)
parser.add_argument(
    "--tls-key",
    type=str,
    help="Key file for TLS, also requires --tls-cert to enable TLS",
    default=None,
)
parser.add_argument(
    "--tls-cert",
    type=str,
    help="Certification file for TLS, also requires --tls-key to enable TLS",
    default=None,
)
parser.add_argument(
    "--gradio-debug",
    action="store_true",
    help="Launch gradio with debug option",
    default=False,
)
parser.add_argument(
    "--server-name", type=str, help="Host name of gradio server", default=None
)
parser.add_argument(
    "--auth",
    type=str,
    nargs="*",
    help='"username:password" pairs to accept in authenication',
    default=None,
)

opts = parser.parse_args()