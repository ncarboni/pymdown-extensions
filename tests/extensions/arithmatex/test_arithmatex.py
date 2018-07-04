"""Test cases for Arithmatex."""
from __future__ import unicode_literals
from ... import util


class TestArithmatex(util.MdCase):
    """Normal test cases for Arithmatex."""

    extension = ['pymdownx.arithmatex']
    extension_configs = {}

    def test_smart_dollar(self):
        """Test smart dollar."""

        self.check_markdown(
            'I have $3.00 and you have $5.00.',
            '<p>I have $3.00 and you have $5.00.</p>'
        )

    def test_escape(self):
        """Test escapes."""

        self.check_markdown(
            r'\$E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j\$',
            r'''<p>$E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j$</p>'''
        )

        self.check_markdown(
            r'\\$3+3$',
            r'<p>\<span><span class="MathJax_Preview">3+3</span><script type="math/tex">3+3</script></span></p>'
        )

        self.check_markdown(
            r'\\\$3+3$',
            r'<p>\$3+3$</p>'
        )

    def test_internal_escaped_dollar(self):
        """Test internally escaped dollars."""

        self.check_markdown(
            r'$\$3.00 + \$5.00 = \$8.00$',
            r'<p><span><span class="MathJax_Preview">\$3.00 + \$5.00 = \$8.00</span>'
            r'<script type="math/tex">\$3.00 + \$5.00 = \$8.00</script></span></p>'
        )

    def test_separated_inline_equations(self):
        """Test that inline equations are kept separate."""

        self.check_markdown(
            r'''
            \(3+3\)
            \\(3+3\)
            \\\(3+3\)
            ''',
            r'''
            <p><span><span class="MathJax_Preview">3+3</span><script type="math/tex">3+3</script></span>
            \(3+3)
            \<span><span class="MathJax_Preview">3+3</span><script type="math/tex">3+3</script></span></p>
            ''',
            True
        )

    def test_block_equations(self):
        """Test block equations."""

        self.check_markdown(
            r'''
            $$
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            $$
            ''',
            r'''
            <div>
            <div class="MathJax_Preview">
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            </div>
            <script type="math/tex; mode=display">
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            </script>
            </div>
            ''',
            True
        )

        self.check_markdown(
            r'''
            \[
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            \]
            ''',
            r'''
            <div>
            <div class="MathJax_Preview">
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            </div>
            <script type="math/tex; mode=display">
            E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
            </script>
            </div>
            ''',
            True
        )

    def test_lists(self):
        """Test in lists."""

        self.check_markdown(
            r'''
            - Here are some more equations:

                $$
                    \begin{align}
                        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                    \end{align}
                $$
            ''',
            r'''
            <ul>
            <li>
            <p>Here are some more equations:</p>
            <div>
            <div class="MathJax_Preview">
                \begin{align}
                    p(v_i=1|\mathbf{h}) &amp; = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                    p(h_j=1|\mathbf{v}) &amp; = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                \end{align}
            </div>
            <script type="math/tex; mode=display">
                \begin{align}
                    p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                    p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                \end{align}
            </script>
            </div>
            </li>
            </ul>
            ''',
            True
        )

        self.check_markdown(
            r'''
            - Inline equations: $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$, \(p(x|y) = \frac{p(y|x)p(x)}{p(y)}\).
            ''',
            r'''
            <ul>
            <li>Inline equations: <span><span class="MathJax_Preview">p(x|y) = \frac{p(y|x)p(x)}{p(y)}</span><script type="math/tex">p(x|y) = \frac{p(y|x)p(x)}{p(y)}</script></span>, <span><span class="MathJax_Preview">p(x|y) = \frac{p(y|x)p(x)}{p(y)}</span><script type="math/tex">p(x|y) = \frac{p(y|x)p(x)}{p(y)}</script></span>.</li>
            </ul>
            ''',  # noqa
            True
        )

    def test_code(self):
        """Test math in code blocks."""

        self.check_markdown(
            r'''
    $$
        \begin{align}
            p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
            p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
        \end{align}
    $$
''',
            self.dedent(
                r'''
                <pre><code>$$
                    \begin{align}
                        p(v_i=1|\mathbf{h}) &amp; = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                        p(h_j=1|\mathbf{v}) &amp; = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                    \end{align}
                $$
                </code></pre>
                ''',
                True
            )
        )

        self.check_markdown(
            r'''
            ```
            $$
                \begin{align}
                    p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                    p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                \end{align}
            $$
            ```
            ''',
            r'''
            <p><code>$$
                \begin{align}
                    p(v_i=1|\mathbf{h}) &amp; = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
                    p(h_j=1|\mathbf{v}) &amp; = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
                \end{align}
            $$</code></p>
            ''',
            True
        )
