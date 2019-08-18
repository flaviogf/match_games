import React, { useEffect, useRef, useState } from 'react';

import { Container, Content } from './styles';

export default function Loader({ visible, onHit }) {
  const [hit, setHit] = useState(false);
  const containerRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      setHit(entries[0].intersectionRatio > 0);
    });

    observer.observe(containerRef.current);

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    onHit();
  }, [hit]);

  return (
    <Container>
      <Content ref={containerRef} visible={visible} />
    </Container>
  );
}
